from pyinfra import host
from pyinfra.operations import apt, server

# Adding tailscale for raspberry pi
apt.key(
  name='Add tailscale key',
  src='https://pkgs.tailscale.com/stable/raspbian/buster.gpg',
)

apt.repo(
  name='Add tailscale repo',
  src='deb https://pkgs.tailscale.com/stable/raspbian buster main',
  filename='tailscale',
)

apt.packages(
  name='Install tailscale',
  packages=['apt-transport-https', 'tailscale'],
  update=True,
)

server.shell(
  name='Start tailscale',
  commands=['tailscale up --authkey {}'.format(host.data.tailscale_preauth_key)]
)