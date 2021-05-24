package storage

import (
	"fmt"
	"log"
	"net/smtp"
)

func bytesInUse(username string) int64 { return 0 }

const sender = "notifications@example.com"
const password = "abcde"
const hostname = "smtp.xxx.com"

const template = `Warning: you are using %d bytes of storage,
%d%% of your quota.`

// 把发邮件函数剥离出来，方便测试替换
var notifyUser = func(username, msg string) {
	auth := smtp.PlainAuth("", sender, password, hostname)
	err := smtp.SendMail(hostname+":587", auth, sender, []string{username}, []byte(msg))

	if err != nil {
		log.Printf("smtp.SendMail(%s) failed: %s", username, err)
	}
}

func CheckQuota(username string) {
	used := bytesInUse(username)
	const quota = 1000000000
	percent := 100 * used / quota
	if percent < 90 {
		return
	}

	msg := fmt.Sprintf(template, used, percent)

	notifyUser(username, msg)
}
