import os

from git import Repo


class JenkinsRepo(Repo):
    def get_tagged_branch(self, commit):
        return [
            n
            for n in self.git.branch("-a", "--contains", commit).splitlines()
            # Example for git branch -a --contains tags/some_tag
            # master
            # rc
            # remotes/origin/HEAD -> origin/master
            # remotes/origin/master
            # remotes/origin/rc
            if "origin" in n and "->" not in n
        ][0].split("/")[2]

    def get_git_data(self):
        """
        Return git repo data.
        In case of branch retun {branch: _name_}
        In case of pr return {pull_request: _number_}
        """

        name = self.git.name_rev("--name-only", "HEAD")
        # posible outputs
        ## local cloned
        # feature/ADH-1376/ADH-1377 #  branches
        # tags/0.1.4 #  tags
        ## jenkins cloned
        # remotes/origin/feature/ADH-1376/ADH-1378 #   branches
        # origin/pr/231/head #  pull requests
        # tags/0.1.4 #  tags
        reponame = self.remotes.origin.url.split("/")[-1].split(".git")[0]
        repoowner = self.remotes.origin.url.split("/")[-2].split(".com:")[-1]

        data = {"reponame": reponame, "repoowner": repoowner}
        if "pipeline" in name:
            reponame = os.getenv("CI_PROJECT_NAME")
            if os.getenv("CI_PIPELINE_SOURCE") == "merge_request_event":
                data.update({"pull_request": os.getenv("CI_MERGE_REQUEST_IID")})
            elif os.getenv("CI_COMMIT_TAG"):
                data.update(
                    {
                        "branch": self.get_tagged_branch(
                            f"tags/{os.getenv('CI_COMMIT_TAG')}"
                        )
                    }
                )
            else:
                data.update({"branch": os.getenv("CI_COMMIT_BRANCH")})
        else:
            # pull request case
            # it works basically on ci with
            # clean git init and fetch remote with +refs/pull/*:refs/origin/pr/*
            # in onther cases with high chance it wont detect pr
            if name.startswith("origin/pr/"):
                data.update({"pull_request": name.split("/")[2]})
                return data

            # tags case
            if name.startswith("tags/"):
                branch = self.get_tagged_branch(name)
            # all others case
            else:
                if name.startswith("remotes/origin/"):
                    branch = name[len("remotes/origin/") :]
                else:
                    branch = name

            data.update({"branch": branch})
        return data
