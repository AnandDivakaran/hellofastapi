FROM debian:13.2

ENV DEBIAN_FRONTEND=noninteractive

# Install system deps in a single RUN and clean up apt lists afterwards
RUN set -eux; \
    apt-get update && \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      git \
      build-essential \
      sudo \
      openssh-client \
      python3 \
      python3-dev \
      python3-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
