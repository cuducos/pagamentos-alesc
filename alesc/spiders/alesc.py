from csv import DictReader
from datetime import date
from decimal import Decimal
from functools import partial
from io import StringIO

from scrapy import Request, Spider

from alesc.items import AlescItem


class AlescSpider(Spider):
    name = 'alesc'
    allowed_domains = ['transparencia.alesc.sc.gov.br']
    main_url = 'http://transparencia.alesc.sc.gov.br/pagamentos_csv.php?periodo='
    description_url = 'http://transparencia.alesc.sc.gov.br/pagamento.php?id='
    available_from = date(2010, 5, 1)
    decimals = (
        'pagamento_rentecao',
        'pagamento_valor_pago',
        'liquidacao_valor',
        'empenho_valor'
    )

    @property
    def start_urls(self):
        today = date.today()
        for year in range(self.available_from.year, today.year + 1):
            for month in range(1, 13):
                dt = date(year, month, 1)
                if self.available_from <= dt <= today:
                    yield f"{self.main_url}{dt.strftime('%m-%Y')}"

    def parse(self, response):
        reader = DictReader(StringIO(response.text), delimiter=';')
        for line in reader:
            data = {
                key.lower().replace('/', '_'): value
                for key, value in line.items()
            }

            for key in self.decimals:
                value = Decimal(data[key].replace('.', '').replace(',', '.'))
                data[key] = value

            url = f'{self.description_url}{data["pagamento_numero"]}'
            kwargs = dict(
                headers={'X-Requested-With': 'XMLHttpRequest'},
                callback=partial(self.parse_description, data)
            )
            yield Request(url, **kwargs)

    def parse_description(self, data, response):
        cells = response.css('td *::text').extract()
        keys, values = cells[3::2], cells[4::2]
        data['descricao'] = dict(zip(keys, values)).get('Descrição')
        yield AlescItem(**data)
