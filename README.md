# VirtualHome

This is a fork to fix some issues starting from [`virtualhome@wah`](https://github.com/xavierpuigf/virtualhome/tree/wah), which is depended by [AutoToM](https://github.com/shunchizhang/online_watch_and_help/tree/AutoToM) and [MindZero](https://github.com/shunchizhang/online_watch_and_help/tree/MindZero).

## Installation

1. Download VirtualHome v2.2.4 executable:
[[Linux]](http://virtual-home.org/release/simulator/v2.0/v2.2.4/linux_exec.zip)
[[MacOS]](http://virtual-home.org/release/simulator/v2.0/v2.2.4/macos_exec.zip)
[[Windows]](http://virtual-home.org/release/simulator/v2.0/v2.2.4/windows_exec.zip)

2. Clone and install `virtualhome` Python library:
   ```sh
   git clone -b wah-fix https://github.com/ShunchiZhang/virtualhome
   cd virtualhome
   pip install -e .
   ```

## Features

- [x] fix agent camera observation ([`18def97`](https://github.com/ShunchiZhang/virtualhome/commit/18def97)), expose default parameters to class attributes for external access ([`72a87bd`](https://github.com/ShunchiZhang/virtualhome/commit/72a87bd))
- [x] support editable installation ([`66aa2e0`](https://github.com/ShunchiZhang/virtualhome/commit/66aa2e0))
- [x] update deprecated function names
  - [x] `collections.Iterable` -> `collections.abc.Iterable` ([`82791b9`](https://github.com/ShunchiZhang/virtualhome/commit/82791b9))
