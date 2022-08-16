// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package algolia

import (
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	provider "github.com/jlmanaloto/terraform-provider-algolia/provider"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

const (
	mainPkg = "algolia"
	mainMod = "index" // the algolia module
)

func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

func Provider() tfbridge.ProviderInfo {
	p := shimv2.NewProvider(provider.New("dev"))

	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "algolia",
		DisplayName: "sw-pulumi-algolia",
		Publisher: "Swarm Work",
		LogoURL: "",
		PluginDownloadURL: "https://github.com/swarm-work/pulumi-algolia/releases",
		Description:       "A Pulumi package for creating and managing algolia cloud resources.",
		Keywords:   []string{"pulumi", "algolia", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/swarm-work/pulumi-algolia",
		GitHubOrg: "jlmanaloto",
		Config:    map[string]*tfbridge.SchemaInfo{
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"algolia_api_key": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ApiKey")},
			"algolia_index":   {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Index")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"algolia_index": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getIndex")},
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
