package main

import (
	"time"

	"github.com/GeertJohan/go.rice/embedded"
)

func init() {

	// define files
	file2 := &embedded.EmbeddedFile{
		Filename:    "post.html",
		FileModTime: time.Unix(1558183796, 0),

		Content: string(""),
	}

	// define dirs
	dir1 := &embedded.EmbeddedDir{
		Filename:   "",
		DirModTime: time.Unix(1558183739, 0),
		ChildFiles: []*embedded.EmbeddedFile{
			file2, // "post.html"

		},
	}

	// link ChildDirs
	dir1.ChildDirs = []*embedded.EmbeddedDir{}

	// register embeddedBox
	embedded.RegisterEmbeddedBox(`theme/default`, &embedded.EmbeddedBox{
		Name: `theme/default`,
		Time: time.Unix(1558183739, 0),
		Dirs: map[string]*embedded.EmbeddedDir{
			"": dir1,
		},
		Files: map[string]*embedded.EmbeddedFile{
			"post.html": file2,
		},
	})
}
