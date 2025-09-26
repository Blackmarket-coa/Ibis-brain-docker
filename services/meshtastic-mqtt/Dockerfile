# Use the official eclipse-mosquitto image as a base
FROM eclipse-mosquitto

# Copy our local configuration file into the correct location inside the image
# This builds the config directly into the image, avoiding volume mount issues.
COPY mosquitto.conf mosquitto/config/mosquitto.conf