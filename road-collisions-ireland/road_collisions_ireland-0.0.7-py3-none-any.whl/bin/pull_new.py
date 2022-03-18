import argparse
import json
import os
import glob

from road_collisions_base import logger

from road_collisions_ireland.models.collision import (
    Collisions,
    Collision
)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--raw-dir',
        dest='raw_dir',
        default=None
    )
    parser.add_argument(
        '--original-file',
        dest='original_file',
        default=None
    )
    args = parser.parse_args()

    collisions = Collisions.from_file(args.original_file)

    logger.info('Loaded %s collisions', (len(collisions)))

    all_ids = set([c.id for c in collisions])
    new_ids = set()

    print('old len: %s' % (len(all_ids)))

    for filename in glob.iglob(os.path.join(args.raw_dir, '**'), recursive=True):
        if os.path.splitext(filename)[-1] != '.json':
            continue

        file_data = json.loads(open(filename).read())
        clean_data = file_data['controls'][3]['layers'][0]['features']

        if len(clean_data) == 0:
            continue

        for d in clean_data:
            point = Collision.parse(d)
            point_id = point.id
            if point_id not in all_ids:
                collisions.append(point)
                all_ids.add(point_id)
                new_ids.add(point_id)

    print('new len: %s' % (len(new_ids)))
    print('ids len: %s' % (len(all_ids)))
    print('fin len: %s' % (len(collisions)))

    with open('/home/rob/road-collisions/resources/ireland.json', 'w') as f:
        f.write(json.dumps([d.serialize() for d in collisions]))


if __name__ == '__main__':
    main()
