CREATE TABLE projetos_inovacao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    categoria VARCHAR(100),
    status VARCHAR(50),
    orcamento NUMERIC,
    data_inicio DATE
);

INSERT INTO projetos_inovacao (nome, categoria, status, orcamento, data_inicio) VALUES
('Sistema de IA para Logística', 'Inteligência Artificial', 'Em andamento', 50000, '2024-01-15'),
('Plataforma de E-learning', 'Educação', 'Concluído', 30000, '2023-08-10'),
('Aplicativo de Saúde', 'Saúde', 'Em andamento', 45000, '2024-03-05'),
('Ferramenta de Automação', 'Automação', 'Planejado', 20000, '2024-06-20'),
('Painel de Análise Financeira', 'Finanças', 'Concluído', 60000, '2023-05-02');
