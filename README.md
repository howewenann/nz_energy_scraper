NZ Energy Scrapper
==============================

a repo containing scripts for scraping the NZ energy site for offer data

Create cookie cutter directory:
    cookiecutter C:\Users\neutr\Documents\projects\pkgs\cookiecutter-data-science-master.zip

Create folders:
    cd nz_energy_scraper
    mkdir envs
    mkdir data

Create environment:
    cd envs
    conda create --prefix spider python=3.7

Activate environment:
    conda activate C:\Users\neutr\Documents\projects\2_personal\repo\nz_energy_scraper\envs\spider

Install packages:
    cd..
    pip install -r requirements.txt
    
Setup scrapy project:
    cd..
    scrapy startproject nz_energy_scraper

Create basic spider:
    cd scrapy_project
    scrapy genspider NZOffers www.emi.ea.govt.nz/Wholesale/Datasets/BidsAndOffers/Offers/2019

Run Spider:
    scrapy crawl NZOffers