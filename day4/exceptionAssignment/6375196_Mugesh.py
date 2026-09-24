enrolled_ids=set()
failed_attempts=0

class EnrollmentError(Exception):
    pass
class InvalidAgeError(EnrollmentError):
    pass
class InvallidFeeError(EnrollmentError):
    pass
class DuplicateEnrollmentError(EnrollmentError):
    pass
class MaxRetriesExceededError(Exception):
    pass

def enroll_learner(learner_id,age,fee,enrolled_ids):
    if learner_id in enrolled_ids:
        raise DuplicateEnrollmentError("Learner Already Enrolled")
    if age <16 or age>65:
        raise InvalidAgeError("Age must be between 16 and 65")
    if fee<1000:
        raise InvallidFeeError("fee must be atleast 1000")
    enrolled_ids.add(learner_id)
    return True

while True:
    try:
        learner_id,age,fee=input("ENter the learner id, age, fee comma seperated: ").split(",")
        learner_id=int(learner_id)
        age=int(age)
        fee=float(fee)
        enroll_learner(learner_id,age,fee,enrolled_ids)
    except ValueError:
        failed_attempts+=1
        print("Please enter valid numbers")
    except EnrollmentError as e:
        failed_attempts+=1
        print("enrollment failed ", e)
    else:
        print("Sucessfull enrollment")
        failed_attempts=0
    finally:
        print("Attempt complete")
    if failed_attempts==3:
        try:
            raise MaxRetriesExceededError()
        except MaxRetriesExceededError:
            print("Too many request go away")
            break