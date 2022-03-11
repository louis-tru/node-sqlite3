{
	"includes": [ "deps/common-sqlite.gypi" ],
	"variables": {
			"sqlite%":"internal",
			"sqlite_libname%":"sqlite3"
	},
	"targets": [
		{
			"target_name": "node-sqlite3",
			"cflags!": [ "-fno-exceptions" ],
			"cflags_cc!": [ "-fno-exceptions" ],
			"xcode_settings": { "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
				"CLANG_CXX_LIBRARY": "libc++",
				"MACOSX_DEPLOYMENT_TARGET": "10.7",
			},
			"msvs_settings": {
				"VCCLCompilerTool": { "ExceptionHandling": 1 },
			},
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")",
				"deps/sqlite3.gyp:sqlite3"
			],
			"sources": [
				"src/backup.cc",
				"src/database.cc",
				"src/node_sqlite3.cc",
				"src/statement.cc"
			],
			"defines": [ "NAPI_VERSION=<(napi_build_version)", "NAPI_DISABLE_CPP_EXCEPTIONS=1" ]
		},
	]
}
