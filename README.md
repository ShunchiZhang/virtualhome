# VirtualHome

This is a fork to fix some issues starting from [`virtualhome@wah`](https://github.com/xavierpuigf/virtualhome/tree/wah), which is depended by [watch_and_help](https://github.com/xavierpuigf/watch_and_help), [online_watch_and_help](https://github.com/xavierpuigf/online_watch_and_help), and [GOMA](https://github.com/lance-ying/GOMA).

## Installation

1. directly install this branch from github under site-packages
   ```sh
   pip install git+https://github.com/ShunchiZhang/virtualhome.git@wah-fix
   ```

2. clone this branch and install editablely
   ```sh
   git clone https://github.com/ShunchiZhang/virtualhome
   cd virtualhome
   git switch wah-fix
   pip install -e .
   ```

## Features

- [x] fix agent camera observation ([`18def97`](https://github.com/ShunchiZhang/virtualhome/commit/18def97)), expose default parameters to class attributes for external access ([`72a87bd`](https://github.com/ShunchiZhang/virtualhome/commit/72a87bd))
- [x] support editable installation ([`66aa2e0`](https://github.com/ShunchiZhang/virtualhome/commit/66aa2e0))
- [x] update deprecated function names
  - [x] `collections.Iterable` -> `collections.abc.Iterable` ([`82791b9`](https://github.com/ShunchiZhang/virtualhome/commit/82791b9))
