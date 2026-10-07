from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status, Query
from app.account.models import User
from app.db.config import SessionDep
from app.product.schemas import PaginatedProductOut, ProductCreate, ProductOut
from app.account.deps import require_admin
from typing import Annotated
from app.product.sevices import create_product, get_all_products,get_product_by_slug,search_product,search_product

router = APIRouter()


@router.post("", response_model=ProductOut)
async def product_create(session: SessionDep,
                         title: str = Form(...),
                         description: str | None = Form(None),
                         price: float = Form(...),
                         stock_quantity: int = Form(...),
                         category_ids: Annotated[list[int], Form()] = [],
                         image: UploadFile | None = File(None),
                         admin_user: User = Depends(require_admin)
                         ):
                        data = ProductCreate(
                                title=title,
                                description=description,
                                price=price,
                                stock_quantity=stock_quantity,
                                category_ids=category_ids
                        )
                        return await create_product(session, data, image)


@router.get("", response_model=PaginatedProductOut)
async def list_product(
        session: SessionDep,
        categories: list[str] | None = Query(default=None),
        limit: int = Query(default=5, ge=1,le=100),
        page: int = Query(default=1, ge=1)
        ):
        return await get_all_products(session, categories, limit, page)




@router.get("/search", response_model=PaginatedProductOut)
async def products_search(session: SessionDep,
                          title: str| None=Query(None),
                          description: str| None = Query(None),
                          min_price: str | None= Query(None),
                          max_price: str | None= Query(None),
                          categories: list[str] | None = Query(default=None),
                          limit: int = Query(default=5, ge=1, le=100),
                          page: int = Query(default=1, ge=1)
                          ):
                return await search_product(
                        session= SessionDep,
                        category_names=categories,
                        title=title,
                        description=description,
                        min_price = min_price,
                        max_price = max_price,
                        limit = limit,
                        page = page 
                )



@router.get("/{slug}", response_model=ProductOut)
async def product_get_by_slug(session: SessionDep, slug= str):
        product = await get_product_by_slug(session, slug)
        if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
        return product


@router.get("/search", response_model=PaginatedProductOut)
async def products_search(
        session: SessionDep,
        categories: list[str] | None = Query(default=None),
        title: str | None = Query(None),
        description: str | None = Query(None),
        min_price: float | None = Query(None),
        max_price: float | None = Query(None),
        limit: int = Query(default=5, ge=1, le=100),
        page: int = Query(default=1, ge=1)
        ):
        return await search_product(
                session=session,
                category_names=categories,
                title=title,
                description=description,
                min_price=min_price,
                max_price=max_price,
                limit=limit,
                page=page
        )
