from fastapi import Depends, HTTPException, status
from ..models import ContactDetails


def create_new_contact_details(contact_details: ContactDetails , db):
    try:
        db.add(contact_details)
        db.commit()
        db.refresh(contact_details)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.orig.pgerror)
    
    return contact_details

def get_contact_details_by_id(id, db):

    cocontact_details = None
    try:
        contact_details = db.query(ContactDetails).filter(ContactDetails.id == id)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, contact_details, e.orig.pgerror)
    
    return contact_details