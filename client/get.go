package client

import (
	"errors"
	"github.com/kainonly/ssh-client/common"
)

// Get ssh client information
func (c *Client) Get(identity string) (content common.Information, err error) {
	if c.options[identity] == nil || c.runtime[identity] == nil {
		err = errors.New("this identity does not exists")
		return
	}
	option := c.options[identity]
	var tunnels []common.TunnelOption
	if c.tunnels[identity] != nil {
		tunnels = *c.tunnels[identity]
	}
	content = common.Information{
		Identity:  identity,
		Host:      option.Host,
		Port:      option.Port,
		Username:  option.Username,
		Connected: string(c.runtime[identity].ClientVersion()),
		Tunnels:   tunnels,
	}
	return
}
