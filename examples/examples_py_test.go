//go:build python || all
// +build python all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestApiKeyPy(t *testing.T) integration.ProgramTestOptions {
	test := getPythonBaseOptions(t).
	        With(integration.ProgramTestOptions{
			Dir:           filepath.Join(getCwd(t), "api-key"),
			RunUpdateTest: true,
		})

	integration.ProgramTest(t, &test)
}

func TestIndexPy(t *testing.T) integration.ProgramTestOptions {
	test := getPythonBaseOptions(t).
		With(integation.ProgramTestOptions{
			Dir:           filepath.Join(getCwd(t), "index"),
			RunUpdateTest: true,
		})

	integration.ProgramTest(t, &test)
}

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	envRegion := getEnvRegion(t)
	base := getBaseOptions()
	pythonBase := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return pythonBase
}
