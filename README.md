# 📊 Dashboard de Inovação

Dashboard interativo desenvolvido em **Python + Streamlit + PostgreSQL** para monitorar projetos de inovação tecnológica.

## 🚀 Tecnologias
- Python 3.10+
- Streamlit
- Pandas
- Plotly
- PostgreSQL

## 📦 Instalação
```bash
git clone https://github.com/seuusuario/dashboard-inovacao.git
cd dashboard-inovacao
pip install -r requirements.txt

Crie um banco PostgreSQL:

sql
Copiar
Editar
CREATE DATABASE inovacao;
Importe os dados iniciais:

bash
Copiar
Editar
psql -U postgres -d inovacao -f data/sample_data.sql
Edite config.py com as credenciais do seu banco.

▶️ Executar
bash
Copiar
Editar
streamlit run app.py
