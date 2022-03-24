import os
import sys

import gitlab

if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile


def download_artifacts(host,
                       token,
                       project_name,
                       project_id,
                       path_save):
    try:
        gl = gitlab.Gitlab(url=host, private_token=token)
        project = None

        if project_name is not None:
            project = gl.projects.get(project_name)

        if project_id is not None:
            project = gl.projects.get(project_id)

        if project is None:
            return None

        pipeline = project.pipelines.list()[0]
        pipeline_job = pipeline.jobs.list()[0]
        job = project.jobs.get(pipeline_job.id, lazy=True)

        zipfn = "___artifacts.zip"

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = './../' + zipfn
        abs_path = os.path.join(script_dir, rel_path)

        with open(path_save + '/' + zipfn, "wb") as f:
            job.artifacts(streamed=True, action=f.write)
        with zipfile.ZipFile(abs_path, 'r') as zip_ref:
            zip_ref.extractall(path_save)
    except Exception as e:
        print("Error:", e)
