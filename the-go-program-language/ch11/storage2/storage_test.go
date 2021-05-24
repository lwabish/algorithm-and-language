package storage

import "testing"

func TestQuotaNotifyUser(t *testing.T) {
	var notifiedUser, notifiedMsg string

	// 备份还原全局变量
	saved := notifyUser
	defer func() { notifyUser = saved }()

	// 这里替换了全局变量，会影响正常流程，所以需要备份还原
	notifyUser = func(user, msg string) {
		notifiedUser, notifiedMsg = user, msg
	}

	const user = "abc@exa.org"
	CheckQuota(user)

	if notifiedUser == "" && notifiedMsg == "" {
		t.Fatalf("notifyUser not called")
	}

	if notifiedUser != user {
		t.Errorf("wrong user (%s) notified, want %s", notifiedUser, user)
	}

}
