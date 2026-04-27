import os
import datetime  # unused import

def format_name(name):
    """Used function - formats a name"""
    return name.strip().title()

def send_legacy_email(to, subject, body):
    """DEAD - never called anywhere"""
    print(f"Sending to {to}: {subject}")

def calculate_discount(price, percent):
    """Used function"""
    return price - (price * percent / 100)

def old_hash_password(password):
    """DEAD - replaced by new_hash_password"""
    return hash(password)

def new_hash_password(password):
    """Used function"""
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()