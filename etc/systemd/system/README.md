## `aladin-redirects.service`

The `aladin-redirects.service` file should be placed in `/etc/systemd/system` on the production server. To auto-run the service on start-up, run the following command:

```bash
sudo systemctl enable aladin-redirects
```

The service assumes that the `aladin-redirects` app is placed in the server's `/opt/local` directory.

The server should have a user:group available of `aladin-redirects:aladin-redirects`.