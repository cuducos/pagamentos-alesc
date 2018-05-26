import scrapy


class AlescItem(scrapy.Item):
	cpf_cnpj = scrapy.Field()
	credor = scrapy.Field()
	empenho_numero = scrapy.Field()
	empenho_modalidade = scrapy.Field()
	empenho_ug = scrapy.Field()
	empenho_fonte_recurso = scrapy.Field()
	empenho_natureza = scrapy.Field()
	empenho_referencia = scrapy.Field()
	empenho_valor = scrapy.Field()
	liquidacao_numero = scrapy.Field()
	liquidacao_emissao = scrapy.Field()
	liquidacao_documento = scrapy.Field()
	liquidacao_valor = scrapy.Field()
	pagamento_numero = scrapy.Field()
	pagamento_ob = scrapy.Field()
	pagamento_pagamento = scrapy.Field()
	pagamento_rentecao = scrapy.Field()
	pagamento_valor_pago = scrapy.Field()
	descricao = scrapy.Field()
