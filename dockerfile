FROM jupyter/scipy-notebook:latest
RUN pip install jupytext \
    && echo 'c.NotebookApp.contents_manager_class="jupytext.TextFileContentsManager"' >> .jupyter/jupyter_notebook_config.py \
    && echo 'c.ContentsManager.default_jupytext_formats = ".ipynb,.Rmd"' >> .jupyter/jupyter_notebook_config.py \
    && rmdir work