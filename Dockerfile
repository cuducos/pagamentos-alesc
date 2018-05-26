FROM continuumio/miniconda3
RUN conda update -y -n base conda && \
    conda install -y scrapy jupyter pandas
WORKDIR /alesc
ADD . .
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root"]
