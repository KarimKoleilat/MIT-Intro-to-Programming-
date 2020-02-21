import ps4c as ps


msg = "hello world!"

sub_msg = ps.SubMessage(msg)

trans_dict = sub_msg.build_transpose_dict("eaiuo")

print(sub_msg.apply_transpose(trans_dict))