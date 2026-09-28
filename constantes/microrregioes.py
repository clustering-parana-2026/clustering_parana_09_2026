"""Registro das microrregiões do Paraná."""

mesorregiao_por_microrregioes_por_municipios: dict[str, dict[str, list]] = {
    'noroeste': {
        'Paranavaí': [
            'Alto Paraná', 'Amaporã', 'Cruzeiro do Sul', 'Diamante do Norte', 'Guairaçá',
            'Inajá', 'Itaúna do Sul', 'Jardim Olinda', 'Loanda', 'Marilena', 'Mirador',
            'Nova Aliança do Ivaí', 'Nova Londrina', 'Paraíso do Norte', 'Paranacity',
            'Paranapoema', 'Paranavaí', 'Planaltina do Paraná', 'Porto Rico',
            'Querência do Norte', 'Santa Cruz de Monte Castelo', 'Santa Isabel do Ivaí',
            'Santa Mônica', 'Santo Antônio do Caiuá', 'São Carlos do Ivaí',
            'São João do Caiuá', 'São Pedro do Paraná', 'Tamboara', 'Terra Rica',
        ],
        'Umuarama': [
            'Alto Paraíso', 'Alto Piquiri', 'Altônia', 'Brasilândia do Sul',
            'Cafezal do Sul', 'Cruzeiro do Oeste', 'Douradina', 'Esperança Nova',
            'Francisco Alves', 'Icaraíma', 'Iporã', 'Ivaté', 'Maria Helena', 'Mariluz',
            'Nova Olímpia', 'Perobal', 'Pérola', 'São Jorge do Patrocínio', 'Tapira',
            'Umuarama', 'Xambrê',
        ],
        'Cianorte': [
            'Cianorte', 'Cidade Gaúcha', 'Guaporema', 'Indianópolis', 'Japurá',
            'Jussara', 'Rondon', 'São Manoel do Paraná', 'São Tomé', 'Tapejara',
            'Tuneiras do Oeste',
        ],
    },
    'centro_ocidental': {
        'Goioerê': [
            'Altamira do Paraná', 'Boa Esperança', 'Campina da Lagoa', 'Goioerê',
            'Janiópolis', 'Juranda', 'Moreira Sales', 'Nova Cantú', 'Quarto Centenário',
            'Rancho Alegre do Oeste', 'Ubiratã',
        ],
        'Campo Mourão': [
            'Araruna', 'Barbosa Ferraz', 'Campo Mourão', 'Corumbataí do Sul',
            'Engenheiro Beltrão', 'Farol', 'Fênix', 'Iretama', 'Luiziana', 'Mamborê',
            'Peabiru', 'Quinta do Sol', 'Roncador', 'Terra Boa',
        ],
    },
    'norte_central': {
        'Astorga': [
            'Ângulo', 'Astorga', 'Atalaia', 'Cafeara', 'Centenário do Sul', 'Colorado',
            'Flórida', 'Guaraci', 'Iguaraçu', 'Itaguajé', 'Jaguapitã', 'Lobato',
            'Lupionópolis', 'Mandaguaçu', 'Munhoz de Melo', 'Nossa Senhora das Graças',
            'Nova Esperança', 'Presidente Castelo Branco', 'Santa Fé', 'Santa Inês',
            'Santo Inácio', 'Uniflor',
        ],
        'Porecatu': [
            'Alvorada do Sul', 'Bela Vista do Paraíso', 'Florestópolis', 'Miraselva',
            'Porecatu', 'Prado Ferreira', 'Primeiro de Maio', 'Sertanópolis',
        ],
        'Floraí': [
            'Doutor Camargo', 'Floraí', 'Floresta', 'Itambé', 'Ivatuba', 'Ourizona',
            'São Jorge do Ivaí',
        ],
        'Maringá': [
            'Mandaguari', 'Marialva', 'Maringá', 'Paiçandu', 'Sarandi',
        ],
        'Apucarana': [
            'Apucarana', 'Arapongas', 'Califórnia', 'Cambira', 'Jandaia do Sul',
            'Marilândia do Sul', 'Mauá da Serra', 'Novo Itacolomi', 'Sabáudia',
        ],
        'Londrina': [
            'Cambé', 'Ibiporã', 'Londrina', 'Pitangueiras', 'Rolândia', 'Tamarana',
        ],
        'Faxinal': [
            'Bom Sucesso', 'Borrazópolis', 'Cruzmaltina', 'Faxinal', 'Kaloré', 'Marumbi',
            'Rio Bom',
        ],
        'Ivaiporã': [
            'Arapuã', 'Ariranha do Ivaí', 'Cândido de Abreu', 'Godoy Moreira',
            'Grandes Rios', 'Ivaiporã', 'Jardim Alegre', 'Lidianópolis', 'Lunardelli',
            'Manoel Ribas', 'Nova Tebas', 'Rio Branco do Ivaí', 'Rosário do Ivaí',
            'São João do Ivaí', 'São Pedro do Ivaí',
        ],
    },
    'norte_pioneiro': {
        'Assaí': [
            'Assaí', 'Jataizinho', 'Nova Santa Bárbara', 'Rancho Alegre',
            'Santa Cecília do Pavão', 'São Jerônimo da Serra',
            'São Sebastião da Amoreira', 'Uraí',
        ],
        'Cornélio Procópio': [
            'Abatiá', 'Andirá', 'Bandeirantes', 'Congonhinhas', 'Cornélio Procópio',
            'Itambaracá', 'Leópolis', 'Nova América da Colina', 'Nova Fátima',
            'Santa Amélia', 'Santa Mariana', 'Santo Antônio do Paraíso', 'Sertaneja',
            'Ribeirão do Pinhal',
        ],
        'Jacarezinho': [
            'Barra do Jacaré', 'Cambará', 'Jacarezinho', 'Jundiaí do Sul',
            'Ribeirão Claro', 'Santo Antônio da Platina',
        ],
        'Ibaiti': [
            'Conselheiro Mairinck', 'Curiúva', 'Figueira', 'Ibaiti', 'Jaboti', 'Japira',
            'Pinhalão', 'Sapopema',
        ],
        'Wenceslau Braz': [
            'Carlópolis', 'Guapirama', 'Joaquim Távora', 'Quatiguá', 'Salto do Itararé',
            'Santana do Itararé', 'São José da Boa Vista', 'Siqueira Campos', 'Tomazina',
            'Wenceslau Braz',
        ],
    },
    'centro_oriental': {
        'Telêmaco Borba': [
            'Imbaú', 'Ortigueira', 'Reserva', 'Telêmaco Borba', 'Tibagi', 'Ventania',
        ],
        'Jaguariaíva': [
            'Arapoti', 'Jaguariaíva', 'Piraí do Sul', 'Sengés',
        ],
        'Ponta Grossa': [
            'Carambeí', 'Castro', 'Palmeira', 'Ponta Grossa',
        ],
    },
    'oeste': {
        'Toledo': [
            'Assis Chateaubriand', 'Diamante do Oeste', 'Entre Rios do Oeste',
            'Formosa do Oeste', 'Guaíra', 'Iracema do Oeste', 'Jesuítas',
            'Marechal Cândido Rondon', 'Maripá', 'Mercedes', 'Nova Santa Rosa',
            'Ouro Verde do Oeste', 'Palotina', 'Pato Bragado', 'Quatro Pontes',
            'Santa Helena', 'São José das Palmeiras', 'São Pedro do Iguaçu',
            'Terra Roxa', 'Toledo', 'Tupãssi',
        ],
        'Cascavel': [
            'Anahy', 'Boa Vista da Aparecida', 'Braganey', 'Cafelândia', 'Campo Bonito',
            'Capitão Leônidas Marques', 'Cascavel', 'Catanduvas', 'Corbélia',
            'Diamante do Sul', 'Guaraniaçu', 'Ibema', 'Iguatu', 'Lindoeste',
            'Nova Aurora', 'Santa Lúcia', 'Santa Tereza do Oeste',
            'Três Barras do Paraná',
        ],
        'Foz do Iguaçu': [
            'Céu Azul', 'Foz do Iguaçu', 'Itaipulândia', 'Matelândia', 'Medianeira',
            'Missal', 'Ramilândia', 'Santa Terezinha de Itaipu', 'São Miguel do Iguaçu',
            'Serranópolis do Iguaçu', 'Vera Cruz do Oeste',
        ],
    },
    'sudoeste': {
        'Capanema': [
            'Ampére', 'Bela Vista da Caroba', 'Capanema', 'Pérola do Oeste', 'Planalto',
            'Pranchita', 'Realeza', 'Santa Izabel do Oeste',
        ],
        'Francisco Beltrão': [
            'Barracão', 'Boa Esperança do Iguaçu', 'Bom Jesus do Sul',
            'Cruzeiro do Iguaçu', 'Dois Vizinhos', 'Enéas Marques',
            'Flor da Serra do Sul', 'Francisco Beltrão', 'Manfrinópolis', 'Marmeleiro',
            'Nova Esperança do Sudoeste', 'Nova Prata do Iguaçu', 'Pinhal de São Bento',
            'Renascença', 'Salgado Filho', 'Salto do Lontra',
            'Santo Antônio do Sudoeste', 'São Jorge do Oeste', 'Verê',
        ],
        'Pato Branco': [
            'Bom Sucesso do Sul', 'Chopinzinho', 'Coronel Vivida', 'Itapejara do Oeste',
            'Mariópolis', 'Pato Branco', 'São João', 'Saudade do Iguaçu', 'Sulina',
            'Vitorino',
        ],
    },
    'centro_sul': {
        'Pitanga': [
            'Boa Ventura de São Roque', 'Laranjal', 'Mato Rico', 'Palmital', 'Pitanga',
            'Santa Maria do Oeste',
        ],
        'Guarapuava': [
            'Campina do Simão', 'Candói', 'Cantagalo', 'Espigão Alto do Iguaçu',
            'Foz do Jordão', 'Goioxim', 'Guarapuava', 'Inácio Martins',
            'Laranjeiras do Sul', 'Marquinho', 'Nova Laranjeiras', 'Pinhão',
            'Porto Barreiro', 'Quedas do Iguaçu', 'Reserva do Iguaçu',
            'Rio Bonito do Iguaçu', 'Turvo', 'Virmond',
        ],
        'Palmas': [
            'Clevelândia', 'Coronel Domingos Soares', 'Honório Serpa', 'Mangueirinha',
            'Palmas',
        ],
    },
    'sudeste': {
        'Prudentópolis': [
            'Fernandes Pinheiro', 'Guamiranga', 'Imbituva', 'Ipiranga', 'Ivaí',
            'Prudentópolis', 'Teixeira Soares',
        ],
        'Irati': [
            'Irati', 'Mallet', 'Rebouças', 'Rio Azul',
        ],
        'União da Vitória': [
            'Bituruna', 'Cruz Machado', 'General Carneiro', 'Paula Freitas',
            'Paulo Frontin', 'Porto Vitória', 'União da Vitória',
        ],
        'São Mateus do Sul': [
            'Antônio Olinto', 'São João do Triunfo', 'São Mateus do Sul',
        ],
    },
    'metropolitana_curitiba': {
        'Cerro Azul': [
            'Adrianópolis', 'Cerro Azul', 'Doutor Ulysses',
        ],
        'Lapa': [
            'Lapa', 'Porto Amazonas',
        ],
        'Curitiba': [
            'Almirante Tamandaré', 'Araucária', 'Balsa Nova', 'Bocaiúva do Sul',
            'Campina Grande do Sul', 'Campo Largo', 'Campo Magro', 'Colombo', 'Contenda',
            'Curitiba', 'Fazenda Rio Grande', 'Itaperuçu', 'Mandirituba', 'Pinhais',
            'Piraquara', 'Quatro Barras', 'Rio Branco do Sul', 'São José dos Pinhais',
            'Tunas do Paraná',
        ],
        'Paranaguá': [
            'Antonina', 'Guaraqueçaba', 'Guaratuba', 'Matinhos', 'Morretes', 'Paranaguá',
            'Pontal do Paraná',
        ],
        'Rio Negro': [
            'Agudos do Sul', 'Campo do Tenente', 'Piên', 'Quitandinha', 'Rio Negro',
            'Tijucas do Sul',
        ],
    },
}