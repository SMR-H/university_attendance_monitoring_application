FROM nginx:alpine

RUN mkdir -p /home/app/staticfiles

# Remove default configuration if it exists
RUN [ -f /etc/nginx/conf.d/default.conf ] && rm /etc/nginx/conf.d/default.conf || echo "default.conf not found"

# Copy your custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/nginx.conf


#-------------------------
# FROM nginx:alpine

# RUN rm /etc/nginx/conf.d/nginx.conf
# COPY nginx.conf /etc/nginx/conf.d