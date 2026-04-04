{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9f090830-07d1-4ec6-90b6-00eee7b1750f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommend(user_id, df, similarity):\n",
    "    \n",
    "    user_loc = df[df['user_id'] == user_id]['location'].values[0]\n",
    "    \n",
    "    similarity_scores = similarity[user_id - 1]\n",
    "    \n",
    "    sorted_scores = sorted(\n",
    "        list(enumerate(similarity_scores)),\n",
    "        key=lambda x: x[1],\n",
    "        reverse=True\n",
    "    )\n",
    "    \n",
    "    filtered_users = []\n",
    "    \n",
    "    for i in sorted_scores:\n",
    "        other_user_id = i[0] + 1\n",
    "        \n",
    "        if other_user_id == user_id:\n",
    "            continue\n",
    "            \n",
    "        other_loc = df[df['user_id'] == other_user_id]['location'].values[0]\n",
    "        \n",
    "        if other_loc == user_loc:\n",
    "            filtered_users.append(other_user_id)\n",
    "        \n",
    "        if len(filtered_users) == 5:\n",
    "            break\n",
    "    \n",
    "    return filtered_users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5a3a0c9-9efa-4cf3-9cd6-37af989b51ed",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
