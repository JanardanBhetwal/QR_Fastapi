from fastapi import APIRouter, Request, Depends, Response
import typing as t

# Remove database and auth-related imports
# from app.db.session import get_db
# from app.db.crud import (
#     get_users,
#     get_user,
#     create_user,
#     delete_user,
#     edit_user,
# )
# from app.db.schemas import UserCreate, UserEdit, User, UserOut
# from app.core.auth import get_current_active_user, get_current_active_superuser

# Sample mock data to replace DB interactions
fake_users_db = [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"},
]

users_router = r = APIRouter()


@r.get(
    "/users",
    response_model=t.List[dict],  # Use plain dict as the response model
    response_model_exclude_none=True,
)
async def users_list(
    response: Response,
    # db=Depends(get_db),  # Remove the DB dependency
    # current_user=Depends(get_current_active_superuser),  # Remove the auth dependency
):
    """
    Get all users (no database)
    """
    # Just return the fake user data
    users = fake_users_db
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(users)}"
    return users


@r.get("/users/me", response_model=dict, response_model_exclude_none=True)
async def user_me(
    # current_user=Depends(get_current_active_user)  # Remove the auth dependency
):
    """
    Get own user (mocked)
    """
    # Just return a mock current user, e.g., Alice
    return fake_users_db[0]  # Return the first user as the current user


@r.get(
    "/users/{user_id}",
    response_model=dict,  # Use plain dict as the response model
    response_model_exclude_none=True,
)
async def user_details(
    request: Request,
    user_id: int,
    # db=Depends(get_db),  # Remove the DB dependency
    # current_user=Depends(get_current_active_superuser),  # Remove the auth dependency
):
    """
    Get any user details (no DB)
    """
    # Find the user in fake_users_db
    user = next((user for user in fake_users_db if user["id"] == user_id), None)
    return user


@r.post("/users", response_model=dict, response_model_exclude_none=True)
async def user_create(
    request: Request,
    user: dict,  # Use plain dict for input as UserCreate schema is removed
    # db=Depends(get_db),  # Remove the DB dependency
    # current_user=Depends(get_current_active_superuser),  # Remove the auth dependency
):
    """
    Create a new user (mocked)
    """
    # Here you would simulate creating a user (just add to fake_users_db for now)
    fake_users_db.append(user)
    return user


@r.put(
    "/users/{user_id}", response_model=dict, response_model_exclude_none=True
)
async def user_edit(
    request: Request,
    user_id: int,
    user: dict,  # Use plain dict for input as UserEdit schema is removed
    # db=Depends(get_db),  # Remove the DB dependency
    # current_user=Depends(get_current_active_superuser),  # Remove the auth dependency
):
    """
    Update existing user (mocked)
    """
    # Find the user and update it
    for idx, existing_user in enumerate(fake_users_db):
        if existing_user["id"] == user_id:
            fake_users_db[idx] = {**existing_user, **user}
            return fake_users_db[idx]
    return None


@r.delete(
    "/users/{user_id}", response_model=dict, response_model_exclude_none=True
)
async def user_delete(
    request: Request,
    user_id: int,
    # db=Depends(get_db),  # Remove the DB dependency
    # current_user=Depends(get_current_active_superuser),  # Remove the auth dependency
):
    """
    Delete existing user (mocked)
    """
    global fake_users_db
    # Find the user and delete it
    fake_users_db = [user for user in fake_users_db if user["id"] != user_id]
    return {"message": f"User with id {user_id} deleted"}
