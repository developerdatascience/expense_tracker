from app.repositories.category_repo import CategoryRepository

class CategoryService:

    def __init__(self, db):
        self.repo = CategoryRepository(db)
    
    def create_category(self, user_id, name):
        return self.repo.create({
            "name": name,
            "user_id": user_id
        })
    
    def list_categories(self, user_id):
        return self.repo.get_by_user(user_id)
    
    def delete_category(self, category_id, user_id):
        return self.repo.delete(category_id, user_id)