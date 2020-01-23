package client

import (
	"github.com/kainonly/ssh-client/common"
	"testing"
)

func TestTesting(t *testing.T) {
	client := New()
	client.Testing(common.ConnectOption{
		Host:       "dell",
		Port:       22,
		Username:   "",
		Password:   "",
		Key:        nil,
		PassPhrase: nil,
	})
}
