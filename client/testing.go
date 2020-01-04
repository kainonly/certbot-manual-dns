package client

import (
	"github.com/kainonly/ssh-client/common"
	"golang.org/x/crypto/ssh"
)

// Test ssh client connection
func (c *Client) Testing(option common.ConnectOption) (sshClient *ssh.Client, err error) {
	return c.connect(option)
}
