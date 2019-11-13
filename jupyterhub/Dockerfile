FROM jupyterhub/jupyterhub:1.0.0

#COPY jupyterhub_config.py .

COPY cull_idle_servers.py .

#RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    dockerspawner==0.10.0 \
    oauthenticator


