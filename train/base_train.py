from datetime import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save_update(self):
        # This method updates the task and sets the updated_at timestamp
        self.updated_at = datetime.now()

    def save_to_dict(self):
        dictFormat = {}

        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            # get the values which are of datetime object type
            if isinstance(val, datetime):
            #convert them to string objects in ISO format
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat

# Create a new task
task = Task("Complete assignment")

# Initially, created_at and updated_at are the same
print("Created At:", task.created_at)
print("Updated At:", task.updated_at)

# Simulate an update by calling save_update
task.save_update()

# Now, updated_at should have the current timestamp
print("Created At:", task.created_at)
print("Updated At:", task.updated_at)
