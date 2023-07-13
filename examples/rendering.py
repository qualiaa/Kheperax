from __future__ import annotations

import jax.random
from matplotlib import pyplot as plt

from kheperax.task import KheperaxConfig, KheperaxTask


def example_usage_render():

    random_key = jax.random.PRNGKey(1)

    random_key, subkey = jax.random.split(random_key)

    task_config = KheperaxConfig.get_default()
    task_config.resolution = (1024, 1024)

    env, policy_network, scoring_fn = KheperaxTask.create_default_task(
        kheperax_config=task_config,
        random_key=subkey,
        episode_length=1000,
        mlp_policy_hidden_layer_sizes=(8,),
    )

    random_key, subkey = jax.random.split(subkey)
    init_state = env.reset(subkey)

    print(init_state.obs)

    img = env.render(init_state)

    plt.imshow(img, origin='lower')
    plt.xticks([])
    plt.yticks([])

    file_name = 'maze.png'
    plt.savefig(file_name)
    print("Saved file:", file_name)


if __name__ == '__main__':
    example_usage_render()
