import amino
client = amino.Client()
client.login(email='ravimourya526@gmail.com',password='ravi1234oppo')
comlist= client.sub_clients(size=100)
for name, id in zip(comlist.name,comlist.comId):
    print("Comm Name  : ",name,"\nComm Id :'166047725',id,"\n--------------")


List of Events
Simple example of how to use this in #aminopy-examples 

on_text_message
on_image_message
on_youtube_message
on_strike_message
on_voice_message
on_sticker_message
on_voice_chat_not_answered
on_voice_chat_not_cancelled
on_voice_chat_not_declined
on_video_chat_not_answered
on_video_chat_not_cancelled
on_video_chat_not_declined
on_avatar_chat_not_answered
on_avatar_chat_not_cancelled
on_avatar_chat_not_declined
on_delete_message
on_group_member_join
on_group_member_leave
on_chat_invite
on_chat_background_changed
on_chat_title_changed
on_chat_icon_changed
on_voice_chat_start
on_video_chat_start
on_avatar_chat_start
on_voice_chat_end
on_video_chat_end
on_avatar_chat_end
on_chat_content_changed
on_screen_room_start
on_screen_room_end
on_chat_host_transfered
on_text_message_force_removed
on_chat_removed_message
on_text_message_removed_by_admin
on_chat_tip
on_chat_pin_announcement
on_voice_chat_permission_open_to_everyone
on_voice_chat_permission_invited_and_requested
on_voice_chat_permission_invite_only
on_chat_view_only_enabled
on_chat_view_only_disabled
on_chat_unpin_announcement
on_chat_tipping_enabled
on_chat_tipping_disabled
on_timestamp_message
on_welcome_message=['setw']
on_invite_message
on_user_typing_start
on_user_typing_end

default (For Other events, will be adding more on the next updates!)
Commit changes
Commit summary
Update bot-detector.py
Optional extended description
Add an optional extended description…
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
