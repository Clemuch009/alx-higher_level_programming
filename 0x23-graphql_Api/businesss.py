from ariadne import QueryType
from  .models import Category, promotion

query = QueryType()

@query.filed("categories")
async def resolve_categories(*_):
    return await Category.query.where(Category.depth == 0)

@query.field("promotions")
async def resolve_promotins(*_):
    return await Promotion.query.all()
