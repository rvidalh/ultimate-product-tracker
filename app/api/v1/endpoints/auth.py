import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.exceptions import EmailAlreadyExistsException
from app.schemas import CreateUserSchema, LoginSchema, UserSchema
from app.services import AuthService, get_auth_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: CreateUserSchema,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        user = await auth_service.register_user(user_data)
        return {
            "message": "User registered successfully",
            "user": UserSchema.model_validate(user),
        }
    except EmailAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error during registration: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@router.post("/login", response_model=UserSchema)
async def login(
    user_data: LoginSchema,
    auth_service: AuthService = Depends(get_auth_service),
):
    user = await auth_service.authenticate_user(user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return UserSchema.model_validate(user)
