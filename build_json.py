import json
import os
import glob
from version import Version
import re

def gen_version_dict(version_full: str, build_dir: str):
    version_dict = {
        'version': version_full,
        'archive': 'version/%s/QuantumESPRESSO.tgz' % get_build_version(build_dir)
    }
    return version_dict

def get_build_version(build_dir: str) -> str:
    return re.search(r'build-([0-9\.]+)/?$', build_dir).group(1)

def get_valid_version(version_str: str, build_dir: str) -> str:
    build_version = get_build_version(build_dir)
    str_version = re.search(r'^([0-9\.]+)', version_str).group(1)
    if Version(build_version, ignore_trailing_zero=True) != Version(str_version, ignore_trailing_zero=True):
        return build_version
    else:
        return version_str

def get_info(build_dir: str):
    docset_json_path = os.path.join(build_dir, 'docset.json')
    if os.path.exists(docset_json_path):
        with open(docset_json_path, encoding='utf8') as fp:
            info = json.load(fp)
            info['version'] = get_valid_version(info['version'], build_dir)
            return info
    else:
        return {
            'version': get_build_version(build_dir)
        }

if __name__ == '__main__':
    builds = glob.glob('tmp/build-*')
    builds, builds_info = zip(*sorted(
        [
            (build_dir, get_info(build_dir)) for build_dir in builds
        ],
        key=lambda item: Version(re.search(r'^([0-9\.]+)', item[1]['version']).group(1)),
        reverse=True))
    final_build_info = builds_info[0]
    final_build_info['specific_versions'] = [
        gen_version_dict(build['version'], build_dir)
        for build, build_dir in zip(builds_info, builds)
    ]
    with open('build/docset.json', 'w', encoding='utf8') as fp:
        json.dump(final_build_info, fp, indent=4)
    