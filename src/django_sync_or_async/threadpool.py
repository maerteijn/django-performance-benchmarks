from concurrent.futures import ThreadPoolExecutor

try:
    from gevent import monkey

    if monkey.is_module_patched("threading"):
        from gevent.threadpool import ThreadPoolExecutor  # noqa
except ImportError:
    pass
