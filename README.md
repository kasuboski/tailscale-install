# tailscale-install
A PyInfra deploy to install and start tailscale.

## Use
* Setup [pyinfra](https://pyinfra.com/)
* Get a [Tailscale Pre-Auth key](https://tailscale.com/kb/1068/acl-tags#pre-authenticated-keys)
* Set the key as the env var `TS_KEY`
* `pyinfra <hosts> --sudo --user=pi install.py`
* 💰💰💰 The hosts should show up in the Tailscale dashboard 💰💰💰

