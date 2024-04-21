mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"23ds1000103@ds.study.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "\
[theme]\n\
backgroundColor='#781f1980'\n\
secondaryBackgroundColor='#d5a54b63'\n\
" > ~/.streamlit/config.toml



