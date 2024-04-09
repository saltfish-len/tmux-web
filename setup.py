from setuptools import setup, find_packages

setup(
    name='tmux-web',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'libtmux==0.36.0',
        'streamlit',
        'streamlit-autorefresh',
        'watchdog'
    ],

    author='Zhanhe Shi',
    author_email='shizhh@shanghaitech.edu.cn',
    description='A web interface for tmux',
    license='MIT',
    keywords='web, tmux, streamlit',
    # tmux-web
    entry_points={
        'console_scripts': [
            'tmux-web = tmux_web.launcher:launch_streamlit'
        ]
    }
)

# set tmux-web='streamlit run app.py'
