FROM jupyter/tensorflow-notebook

LABEL maintainer="windwood-xmu <windwood@xmu.edu.cn>"

# Upgrade Tensorflow to 2.0
RUN conda install --quiet --yes \
    'tensorflow=2*' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

