# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.241.1/containers/python-3/.devcontainer/base.Dockerfile

# 3.7 recommended by Google for GCP SDK: https://cloud.google.com/sdk/docs/install
ARG VARIANT="3.7-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install GCP SDK
# Adapted from https://gist.github.com/omidmt/65c8382db828fb7a5b5034e5906389b6
RUN curl -sSL https://sdk.cloud.google.com > /tmp/install.sh && bash /tmp/install.sh --install-dir=/workspaces --disable-prompts

RUN echo "" >> /home/vscode/.bashrc
RUN echo "# The next line updates PATH for the Google Cloud SDK." >> /home/vscode/.bashrc
RUN echo "if [ -f '/workspaces/google-cloud-sdk/path.bash.inc' ]; then . '/workspaces/google-cloud-sdk/path.bash.inc'; fi" >> /home/vscode/.bashrc
RUN echo "" >> /home/vscode/.bashrc
RUN echo "# The next line enables shell command completion for gcloud." >> /home/vscode/.bashrc
RUN echo "if [ -f '/workspaces/google-cloud-sdk/completion.bash.inc' ]; then . '/workspaces/google-cloud-sdk/completion.bash.inc'; fi" >> /home/vscode/.bashrc

ENV PATH $PATH:/workspaces/google-cloud-sdk/bin

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1