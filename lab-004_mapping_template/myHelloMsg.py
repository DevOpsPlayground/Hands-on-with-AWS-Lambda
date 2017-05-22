def lambda_handler(event, context):
    # TODO implement
    print("Event is %s" % event)
    name = event.get("name") or "No msg submitted"
    return "Hello from Lambda: %s " % (name)
