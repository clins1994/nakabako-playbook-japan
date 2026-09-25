# SPDX-License-Identifier: MIT
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class InstallerTests(unittest.TestCase):
    def test_opt_out_is_forced_and_caller_project_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            fake = base / 'npx'
            fake.write_text('#!/usr/bin/env python3\nimport os,sys,json\nprint(json.dumps({"args":sys.argv[1:],"cwd":os.getcwd(),"disable":os.environ.get("DISABLE_TELEMETRY"),"dnt":os.environ.get("DO_NOT_TRACK")}))\n')
            fake.chmod(0o700)
            env = dict(os.environ, PATH=str(base)+os.pathsep+os.environ['PATH'], DISABLE_TELEMETRY='', DO_NOT_TRACK='')
            result = subprocess.run(['bash', str(ROOT/'install.sh'), '--agent', 'codex'], cwd=base, env=env, text=True, capture_output=True, check=True)
            data = json.loads(result.stdout)
            self.assertEqual(data['disable'], '1')
            self.assertEqual(data['dnt'], '1')
            self.assertEqual(data['cwd'], str(base))
            self.assertEqual(data['args'], ['--yes','skills@1.7.0','add',str(ROOT),'--skill','health-checkup','--copy','--agent','codex'])
