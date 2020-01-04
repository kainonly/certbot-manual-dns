package storage

import (
	"github.com/kainonly/ssh-client/common"
	"github.com/syndtr/goleveldb/leveldb"
	"github.com/vmihailenco/msgpack"
	"log"
)

type (
	ConfigOption struct {
		Connect map[string]*common.ConnectOption
		Tunnel  map[string]*[]common.TunnelOption
	}
)

var db *leveldb.DB

// Initialize leveldb
func InitLevelDB(path string) {
	var err error
	db, err = leveldb.OpenFile(path, nil)
	if err != nil {
		log.Fatalln(err)
	}
}

// Set up temporary storage
func SetTemporary(config ConfigOption) (err error) {
	data, err := msgpack.Marshal(config)
	err = db.Put([]byte("temporary"), data, nil)
	return
}

// Get temporary storage
func GetTemporary() (config ConfigOption, err error) {
	exists, err := db.Has([]byte("temporary"), nil)
	if exists == false {
		config = ConfigOption{}
		return
	}
	data, err := db.Get([]byte("temporary"), nil)
	err = msgpack.Unmarshal(data, &config)
	return
}
