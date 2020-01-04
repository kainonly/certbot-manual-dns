package client

import (
	"github.com/kainonly/ssh-client/storage"
)

// Delete ssh client
func (c *Client) Delete(identity string) (err error) {
	if c.options[identity] == nil || c.runtime[identity] == nil {
		return
	}
	if c.tunnels[identity] != nil {
		c.closeTunnel(identity)
	}
	if c.runtime[identity] != nil {
		c.runtime[identity].Close()
	}
	delete(c.runtime, identity)
	delete(c.options, identity)
	err = storage.SetTemporary(storage.ConfigOption{
		Connect: c.options,
		Tunnel:  c.tunnels,
	})
	return
}
