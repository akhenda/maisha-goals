import functools
from flask import url_for, request
from ..exceptions import ValidationError


def paginate(collection, max_per_page=20):
    """Generate a paginated response for a resource collection.

    Routes that use this decorator must return a SQLAlchemy query as a
    response.

    The output of this decorator is a Python dictionary with the paginated
    results. The application must ensure that this result is converted to a
    response object, either by chaining another decorator or by using a
    custom response object that accepts dictionaries."""
    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            # invoke the wrapped function
            query = f(*args, **kwargs)

            # obtain pagination arguments from the URL's query string
            page = request.args.get('page', 1, type=int)
            if request.args and (not request.args.get('limit') and not request.args.get('q') and not request.args.get('expanded') and not request.args.get('page')):
                raise ValidationError('invalid query parameter')
            elif request.args.get('limit'):
                try:
                    limit = int(request.args.get('limit'))
                except:
                    raise ValidationError('limit query parameter only accepts integers')
            limit = min(request.args.get('limit', max_per_page,
                                         type=int), max_per_page)
            expanded = 1
            if request.args.get('expanded', 0, type=int) != 0:
                expanded = 1

            # run the query with Flask-SQLAlchemy's pagination
            p = query.paginate(page, limit)

            # build the pagination metadata to include in the response
            pages = {'page': page, 'limit': limit,
                     'total': p.total, 'pages': p.pages}
            if p.has_prev:
                pages['prev_url'] = url_for(request.endpoint, page=p.prev_num,
                                            limit=limit,
                                            expanded=expanded, _external=True,
                                            **kwargs)
            else:
                pages['prev_url'] = None
            if p.has_next:
                pages['next_url'] = url_for(request.endpoint, page=p.next_num,
                                            limit=limit,
                                            expanded=expanded, _external=True,
                                            **kwargs)
            else:
                pages['next_url'] = None
            pages['first_url'] = url_for(request.endpoint, page=1,
                                         limit=limit, expanded=expanded,
                                         _external=True, **kwargs)
            pages['last_url'] = url_for(request.endpoint, page=p.pages,
                                        limit=limit, expanded=expanded,
                                        _external=True, **kwargs)

            # generate the paginated collection as a dictionary
            if expanded:
                results = [item.export_data() for item in p.items]
            else:
                results = [item.get_url() for item in p.items]

            # return a dictionary as a response
            return {collection: results, 'pages': pages}
        return wrapped
    return decorator
