from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = self.get_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_topic(topic_id)
        topic.storage_folder = new_storage_folder
        topic.topic = new_topic

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove(self.get_category(category_id))

    def delete_topic(self, topic_id):
        self.topics.remove(self.get_topic(topic_id))

    def delete_document(self, document_id):
        self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id: int):
        return next(filter(lambda d: d.id == document_id, self.documents))

    def get_topic(self, topic_id: int):
        return next(filter(lambda t: t.id == topic_id, self.topics))

    def get_category(self, category_id: int):
        return next(filter(lambda c: c.id == category_id, self.categories))

    def __repr__(self):
        return "\n".join({str(d) for d in self.documents})
