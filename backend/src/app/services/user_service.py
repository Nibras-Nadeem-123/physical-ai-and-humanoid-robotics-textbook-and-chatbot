from uuid import UUID
from datetime import datetime
from backend.src.app.models import User # Assuming User model is defined here

# This is a very basic placeholder for a user service that would
# interact with a database (e.g., PostgreSQL).

_mock_users_db = {} # In-memory mock database for demonstration

class UserService:
    def get_user_by_id(self, user_id: UUID) -> User | None:
        return _mock_users_db.get(str(user_id))

    def update_user_consent(self, user_id: UUID, consent_status: bool) -> User | None:
        user = self.get_user_by_id(user_id)
        if user:
            user.consent_status = consent_status
            _mock_users_db[str(user_id)] = user
            return user
        return None

    def create_user(self, user_id: UUID, auth_id: str, email: str = None) -> User:
        user = User(
            id=user_id,
            auth_id=auth_id,
            email=email,
            created_at=datetime.utcnow(),
            last_login_at=datetime.utcnow(),
            consent_status=False # Default to false on creation
        )
        _mock_users_db[str(user_id)] = user
        return user

user_service = UserService()
