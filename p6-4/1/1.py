def is_context_manager(obj):
    return all((
            '__enter__' in dir(obj), 
            '__exit__' in dir(obj),
        ))